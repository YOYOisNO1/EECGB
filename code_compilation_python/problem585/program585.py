def program585():
    use std::io;
    use std::io::Read;
    
    fn main() {
        let mut buffer = String::new();
        io::stdin().read_to_string(&mut buffer).unwrap();
        let mut cin = buffer.split_whitespace().map(|x| x.parse::<u64>().unwrap());
        let n = cin.next().unwrap() as usize;
        let mut a = cin.enumerate().collect::<Vec<_>>();
        a.sort_by_key(|x| x.1);
        for i in 0..n / 2 {
            println!("{} {}", a[i].0 + 1, a[n - i - 1].0 + 1);
        }
    }