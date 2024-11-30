use std::fs::File;
use std::io::{BufRead, BufReader};


fn read_lines(path: &str) -> Vec<String> {
    let input = File::open(path).expect("Failed to open file");
    let buffer = BufReader::new(input);

    buffer.lines()
          .map(|line| line.expect("Failed to parse line" ))
          .collect::<Vec<String>>()
}

fn solve_1(commands: &Vec<String>) -> i32 {
    let mut x: i32 = 0;
    let mut depth: i32 = 0;

    for command in commands.iter() {
        let mut command_iter = command.split_whitespace();
        let cmd: &str = command_iter.next().unwrap();
        let value: i32 = match command_iter.next() {
            Some(s) => { s.parse().unwrap() },
            None => { panic!("Failed to parse value as int"); }
        };
        
        match cmd {
            "forward" => { x += value; },
            "down" => { depth += value; },
            "up" => { depth -= value; },
            _ => { panic!("Invalid command!"); }
        };
    };

    x * depth
}

fn solve_2(commands: &Vec<String>) -> i32 {
    let mut x: i32 = 0;
    let mut depth: i32 = 0;
    let mut aim: i32 = 0;

    for command in commands.iter() {
        let mut command_iter = command.split_whitespace();
        let cmd: &str = command_iter.next().unwrap();
        let value: i32 = match command_iter.next() {
            Some(s) => { s.parse().unwrap() },
            None => { panic!("Failed to parse value as int"); }
        };
        
        match cmd {
            "forward" => { x += value; depth += aim * value;},
            "down" => { aim += value; },
            "up" => { aim -= value; },
            _ => { panic!("Invalid command!"); }
        };
    };

    x * depth
}

fn main() {
    let path = "input.txt";
    let commands = read_lines(path);

    let result = solve_1(&commands);
    println!("Problem 1: {}", result);
    let result = solve_2(&commands);
    println!("Problem 2: {}", result);
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve_1() {
        let commands = read_lines("example.txt");
        let count = solve_1(&commands);
        assert_eq!(count, 150);
    }

    #[test]
    fn test_solve_2() {
        let commands = read_lines("example.txt");
        let count = solve_2(&commands);
        assert_eq!(count, 900);
    }
}
