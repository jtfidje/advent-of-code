// I couldn't solve Part 2, so I had to use brute force....

fn main() {
    let gears: [u64; 5] = [15871, 16409, 18023, 12643, 19099];
    let inc: u64 = 21251;
    let mut counter: u64 = 21251;
    
    let loop_size: u64 = 1_000_000_000;

    for _ in 1..loop_size {
        let mut finished = true;
        for gear in gears {
                if counter % gear != 0 {
                    finished = false;
                    break
                }
        }

        if finished == true {
            println!("{}", counter);
            break
        }

        counter += inc;
    }

}
