use base64::decode;
use num_bigint::BigUint;
use std::fs::File;
use std::io::{self, BufRead, BufReader, Read, Result, Write};
use std::process::{Command, Stdio};

fn main() -> Result<()> {
    let mut rng = File::open("/dev/urandom")?;

    /* Randomly decide how many bytes to generate */
    let mut buffer = [0u8; 1];
    rng.read_exact(&mut buffer)?;

    let mut n_bytes = u8::from_be_bytes(buffer);
    if n_bytes < 2 {
        n_bytes = 2;
    }
    let mut buffer2: Vec<u8> = Vec::with_capacity(n_bytes as usize);
    buffer2.resize(n_bytes as usize, 0);
    rng.read_exact(&mut buffer2)?;
    let mid = n_bytes as usize / 2;
    println!(
        "{} {} {:?} {}",
        buffer2.len(),
        buffer2.capacity(),
        n_bytes,
        mid
    );
    let split = buffer2.split_at(mid);

    let a = BigUint::from_bytes_be(split.0);
    let b = BigUint::from_bytes_be(split.1);
    let res = &a * &b;
    //println!("{}", res);
    let res_encoded = res.to_bytes_be();

    let mut bigintpy = Command::new("python3")
        .arg("bigint.py")
        .stdout(Stdio::piped()) // Capture stdout
        .stdin(Stdio::piped()) // Capture stdin
        .spawn()
        .expect("Failed to start process");

    if let Some(mut stdin) = bigintpy.stdin.take() {
        writeln!(stdin, "mult").unwrap();
        writeln!(stdin, "{}", base64::encode(&a.to_bytes_be())).unwrap();
        writeln!(stdin, "{}", base64::encode(&b.to_bytes_be())).unwrap();
    }

    if let Some(stdout) = bigintpy.stdout.take() {
        let reader = BufReader::new(stdout);
        for line in reader.lines().take(1) {
            match line {
                Ok(text) => {
                    let decoded = decode(text).unwrap();
                    assert!(decoded == res_encoded);
                }
                Err(e) => eprintln!("Error reading line: {}", e),
            }
        }
    }

    Ok(())
}
