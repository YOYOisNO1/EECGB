def program1265():
    using System;
    
    class Program
    {
      static void Main()
      {
        int a = int.Parse(Console.ReadLine());
        int b = int.Parse(Console.ReadLine());
        int i = 0;
        while(a <= b)
        {
          a = a*3;
          b = b*2;
          i = i+1;
        }
        Console.Write(i);
      }
    }