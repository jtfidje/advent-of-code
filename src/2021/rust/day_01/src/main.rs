use std::fs::File;
use std::io::{BufReader, BufRead};

fn read_lines(path: &str) -> Vec<String> {
    let file = File::open(path).expect("Failed to open file");
    let buf = BufReader::new(file);

    buf.lines()
       .map(|line| line.expect("Could not parse line"))
       .collect()
}

fn solve_1(measurements: &Vec<i32>) -> i32 {
    let mut count: i32 = 0;
    for i in 1..measurements.len() {
        if measurements[i] > measurements[i - 1] {
            count += 1;
        }
    }
    count
}

fn solve_2(measurements: &Vec<i32>) -> i32 {
    let mut count: i32 = 0;

    for i in 0..(measurements.len() - 3) {
        let win_1: i32 = measurements[i..=i + 2].iter().sum();
        let win_2: i32 = measurements[i + 1..=i + 3].iter().sum();

        if win_2 > win_1 {
            count += 1;
        }
    }
    count
}

fn main() {
    let lines = read_lines("input.txt");
    let measurements: Vec<i32> = lines.iter()
                                      .map(|line| line.parse().unwrap())
                                      .collect();

    let count = solve_1(&measurements);
    println!("There are {} measurements that's larger than the previous!", count);
    
    let count = solve_2(&measurements);
    println!("There are {} measurement windows that's larger than the previous!", count);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve_1() {
        let lines = read_lines("example.txt");
        let measurements: Vec<i32> = lines.iter()
                                        .map(|line| line.parse().unwrap())
                                        .collect();

        let count = solve_1(&measurements);
        assert_eq!(count, 7);
    }

    #[test]
    fn test_solve_2() {
        let lines = read_lines("example.txt");
        let measurements: Vec<i32> = lines.iter()
                                        .map(|line| line.parse().unwrap())
                                        .collect();

        let count = solve_2(&measurements);
        assert_eq!(count, 5);
    }
}