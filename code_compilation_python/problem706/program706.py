    object CF333A {
    def main(argv: Array[String]) {
        def calc(n: Int): Int = {
                if (n % 3 == 0) calc(n / 3)
                else (n + 2) / 3
            }
            println(calc(readLine.toInt))
        }
    }