use::std::fs::File;
use::std::io::{BufRead, BufReader};


fn read_lines(path: &str) -> Vec<Vec<char>> {
    let input = File::open(path).expect("Failed to open file");
    let buffer = BufReader::new(input);

    buffer.lines()
          .map(|line| line.expect("Failed to parse line").chars().collect())
          .collect::<Vec<Vec<char>>>()
}


fn solve_1(report: &Vec<Vec<char>>) -> i32 {
    let line_len = report[0].len();
    
    // Count bits in positions
    let mut bits: Vec<[u32; 2]> = vec![[0, 0]; line_len];
    for i in 0..line_len {

        for line in report.iter() {
            
            match line[i] {
                '0' => bits[i][0] += 1,
                '1' => bits[i][1] += 1,
                _ => {}
            }
        }
    }

    let mut gamma: Vec<i32> = Vec::new();
    let mut epsilon: Vec<i32> = Vec::new();

    // Calculate Gamma & Epsilon
    for elem in bits.iter() {
        if elem[0] > elem[1] {
            // 0 is most common
            gamma.push(0);
            epsilon.push(1);
        } else {
            gamma.push(1);
            epsilon.push(0);
        }
    }

        gamma.into_iter().fold(0, |acc, bit| (acc << 1) + bit) * 
        epsilon.into_iter().fold(0, |acc, bit| (acc << 1) + bit)

}


fn solve_2(report: &Vec<Vec<char>>) -> i32 {
    let line_len = report[0].len();
    // Count bits in positions
    let mut bits: Vec<[u32; 2]> = vec![[0, 0]; line_len];
    for i in 0..line_len {

        for line in report.iter() {
            
            match line[i] {
                '0' => bits[i][0] += 1,
                '1' => bits[i][1] += 1,
                _ => {}
            }
        }
    }

    let most_significant: Vec<char> = bits.iter().map(|line| if line[0] < line[1] { '1' } else { '0' }).collect();
    let least_significant: Vec<char> = bits.iter().map(|line| if line[1] > line[0] { '0' } else { '1' }).collect();

    let mut o2_temp: Vec<Vec<char>> = report.clone();
    let mut co2_temp: Vec<Vec<char>> = report.clone();

    for i in 0..line_len {
        for j in (0..o2_temp.len()).rev() {
            if o2_temp[j][i] != most_significant[i] {
                o2_temp.remove(j);
            }
        }

        if o2_temp.len() == 1 { break }
    }

    for i in 0..line_len {
        for j in (0..co2_temp.len()).rev() {
            if co2_temp[j][i] != least_significant[i] {
                co2_temp.remove(j);
            }
        }

        if co2_temp.len() == 1 { break }
    }

    let o2: Vec<i32> = o2_temp[0].iter().map(|c| if *c == '1' { 1 } else { 0 }).collect();
    let co2: Vec<i32> = co2_temp[0].iter().map(|c| if *c == '1' { 1 } else { 0 }).collect();

    o2.into_iter().fold(0, |acc, bit| (acc << 1) + bit) *
    co2.into_iter().fold(0, |acc, bit| (acc << 1) + bit)
}

fn main() {
    let path = "input.txt";
    let report = read_lines(path);
    let solution_1 = solve_1(&report);
    println!("Solution 1: {}", solution_1); 

    let solution_2 = solve_2(&report);
    println!("Solution 2: {}", solution_2);
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve_1() {
        let report = read_lines("example.txt");
        let result = solve_1(&report);
        assert_eq!(result, 198);
    }

    #[test]
    fn test_solve_2() {
        let report = read_lines("example.txt");
        let result = solve_2(&report);
        assert_eq!(result, 230)
    }
}
