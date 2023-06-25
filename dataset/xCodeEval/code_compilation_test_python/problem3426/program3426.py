def program3426():
    ﻿using System;
    using System.Collections.Generic;
    using System.Globalization;
    using System.IO;
    using System.Linq;
    using System.Text;
    public class Codeforces
    {
        protected static TextReader reader;
        protected static TextWriter writer;
        static void Main()
        {
            reader = new StreamReader(Console.OpenStandardInput(1024 * 10), System.Text.Encoding.ASCII, false, 1024 * 10);
            writer = new StreamWriter(Console.OpenStandardOutput(1024 * 10), System.Text.Encoding.ASCII, 1024 * 10);
            var n = ReadInt();
            var bak = n;
            var s = ReadToken();
            var ans = new string[100];
            int ind = 0;
            var alpha = Enumerable.Repeat(1, 26).ToArray();
            for (int i = 0; i < s.Length - 1; i++)
            {
                int j = i;
                if (s[i] != s[i + 1] && alpha[s[i] - 'a'] > 0)
                {
                    if (n == 1)
                    {
                        ans[ind] = s.Substring(j);
                    }
                    else
                    {
                        ans[ind++] = s[i].ToString();
                    }
                    alpha[s[i] - 'a']--;
                    n--;
                }
                else
                {
                    for (j = i + 2; j < s.Length; j++)
                    {
                        if (s[i] != s[j] && alpha[s[i] - 'a'] > 0)
                        {
                            if (n == 1)
                            {
                                ans[ind] = s.Substring(j);
                            }
                            else
                            {
                                ans[ind++] = s.Substring(i, j - i);
                            }
                            alpha[s[i] - 'a']--;
                            n--;
                            i = j - 1;
                            break;
                        }
                    }
                }
                if (n == 0)
                {
                    Console.WriteLine("YES");
                    for (int k = 0; k < bak; k++)
                    {
                        Console.WriteLine(ans[k]);
                    }
                    return;
                }
            }
            Console.WriteLine("NO");
            reader.Close();
            writer.Close();
        }
        #region Read / Write
    
        private static Queue<string> currentLineTokens = new Queue<string>();
    
        private static string[] ReadAndSplitLine()
        {
            return reader.ReadLine().Split(new[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
        }
    
        public static string ReadToken()
        {
            while (currentLineTokens.Count == 0)
                currentLineTokens = new Queue<string>(ReadAndSplitLine());
            return currentLineTokens.Dequeue();
        }
    
        public static int ReadInt()
        {
            return int.Parse(ReadToken());
        }
    
        public static long ReadLong()
        {
            return long.Parse(ReadToken());
        }
    
        public static double ReadDouble()
        {
            return double.Parse(ReadToken(), CultureInfo.InvariantCulture);
        }
    
        public static int[] ReadIntArray()
        {
            return ReadAndSplitLine().Select(int.Parse).ToArray();
        }
    
        public static long[] ReadLongArray()
        {
            return ReadAndSplitLine().Select(long.Parse).ToArray();
        }
    
        public static double[] ReadDoubleArray()
        {
            return ReadAndSplitLine().Select(s => double.Parse(s, CultureInfo.InvariantCulture)).ToArray();
        }
        public static int[][] ReadIntMatrix(int numberOfRows)
        {
            int[][] matrix = new int[numberOfRows][];
            for (int i = 0; i < numberOfRows; i++)
                matrix[i] = ReadIntArray();
            return matrix;
        }
        public static int[][] ReadAndTransposeIntMatrix(int numberOfRows)
        {
            int[][] matrix = ReadIntMatrix(numberOfRows);
            int[][] ret = new int[matrix[0].Length][];
            for (int i = 0; i < ret.Length; i++)
            {
                ret[i] = new int[numberOfRows];
                for (int j = 0; j < numberOfRows; j++)
                    ret[i][j] = matrix[j][i];
            }
            return ret;
        }
    
        public static string[] ReadLines(int quantity)
        {
            string[] lines = new string[quantity];
            for (int i = 0; i < quantity; i++)
                lines[i] = reader.ReadLine().Trim();
            return lines;
        }
        public static void WriteArray<T>(IEnumerable<T> array)
        {
            writer.WriteLine(string.Join(" ", array));
        }
    
        public static void Write<T>(params T[] array)
        {
            WriteArray(array);
        }
    
        public static void WriteLines<T>(IEnumerable<T> array)
        {
            foreach (var a in array)
                writer.WriteLine(a);
        }
        #endregion
    }