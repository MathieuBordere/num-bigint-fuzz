use std::io::{self, Write};
use std::process::Command;

fn main() {
    let output = Command::new("python")
        .arg("bigint.py")
        .output()
        .expect("failed to execute process");

    println!("status: {}", output.status);
    io::stdout().write_all(&output.stdout).unwrap();
    io::stderr().write_all(&output.stderr).unwrap();

    assert!(output.status.success());
}
