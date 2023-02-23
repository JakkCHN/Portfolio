//Programming Assisgnment
//C# Hangmann Simple Mini Game programm

using System;
using System.Collections.Generic;
using static System.Random;                                                     ////to be able to use list
using System.Text;

namespace HangmanGame
{
    internal class Programw
    {
        private static void printHangman(int wrong)
        {
            if (wrong == 0)
            {
                Console.WriteLine("\n+---+");                                //Frame for the Stickman
                Console.WriteLine("     |");
                Console.WriteLine("     |");
                Console.WriteLine("     |");
                Console.WriteLine("    ===");
            }
            else if (wrong == 1)
            {
                Console.WriteLine("\n+---+");                                //with each guess prints a new character to make the stickman
                Console.WriteLine(" O   |");
                Console.WriteLine("     |");                                //head
                Console.WriteLine("     |");
                Console.WriteLine("    ===");
            }
            else if (wrong == 2)
            {
                Console.WriteLine("\n+---+");
                Console.WriteLine(" 0   |");                                 //body
                Console.WriteLine(" |   |");
                Console.WriteLine("     |");
                Console.WriteLine("    ===");
            }
            else if (wrong == 3)
            {
                Console.WriteLine("\n+---+");
                Console.WriteLine(" 0   |");                                 //arm
                Console.WriteLine("/|   |");
                Console.WriteLine("     |");
                Console.WriteLine("    ===");
            }
            else if (wrong == 4)
            {
                Console.WriteLine("\n+---+");
                Console.WriteLine(" 0   |");                                 //arm
                Console.WriteLine("/|\\ |");
                Console.WriteLine("     |");
                Console.WriteLine("    ===");
            }
            else if (wrong == 5)
            {
                Console.WriteLine("\n+---+");
                Console.WriteLine(" 0   |");                                 //leg
                Console.WriteLine("/|\\ |");
                Console.WriteLine("/    |");
                Console.WriteLine("    ===");
            }
            else if (wrong == 6)
            {
                Console.WriteLine("\n+---+");
                Console.WriteLine(" 0   |");
                Console.WriteLine("/|\\ |");                                //leg
                Console.WriteLine("/ \\ |");
                Console.WriteLine("    ===");
            }

        }
                                                                                                //Funtion to display word
        private static int printWord(List<char> guessedLetters, string randomWord)              //Random word will be generated from a list specified furthur down
        {                                                                                      
            int counter = 0;
            int rightLetters = 0;
            Console.Write("\r\n");
            foreach (char c in randomWord)
            {
                if (guessedLetters.Contains(c))                                               //if letter is right then it will print it 
                {
                    Console.Write(c + " ");
                    rightLetters++;
                }
                else
                {
                    Console.Write(" ");
                }
                counter++;
            }
            return rightLetters;
        }

        private static void printLines(string randomWord)                                    //funtion to print out the lines under letters
        {
            Console.Write("\r");
            foreach (char c in randomWord)
            {
                Console.OutputEncoding = System.Text.Encoding.Unicode;                       //prints the lined under the number on the same line
                Console.Write("\u0305 ");
            }
        }

        static void Main(string[] args)                                                      //start of logic that runs the game
        {
            Console.WriteLine("C# Programme Assisnment");
            Console.WriteLine("Welcome to a Simple Game of Hangman");
            Console.WriteLine("-----------------------------------------------------");

            Random random = new Random();
            List<String> wordDictionary = new List<string> { "sheffield", "hallam", "Glasses", "coding", "fire", "smile", "angel", "water", "knight", "diamond" };
            int index = random.Next(wordDictionary.Count);                                            //list of words for the game to use randomly
            string randomWord = wordDictionary[index];

            foreach (char x in randomWord)
            {
                Console.Write("_ ");                                                          //Prints out the lines for the Random word to guess
            }

            int lengthOfWordToGuess = randomWord.Length;
            int amountOfTimesWrong = 0;                                                        //Kepp track on ammount of times the user is wrong
            List<char> currentLettersGuessed = new List<char>();                              //keep track on ammount of times the user is right
            int currentLettersRight = 0;

            while (amountOfTimesWrong != 6 && currentLettersRight != lengthOfWordToGuess)
            {
                Console.Write("\nLetters guessed so far: ");
                foreach (char letter in currentLettersGuessed)
                {
                    Console.Write(letter + " ");
                }
                Console.Write("\nGuess a letter: ");                                                                         //Asking user for an input 
                char letterGuessed = Console.ReadLine()[0];
                if (currentLettersGuessed.Contains(letterGuessed))                                                           //Check if letter has already been guessed
                {
                    Console.Write("\r\nLetter already guessed.");
                    printHangman(amountOfTimesWrong);
                    currentLettersRight = printWord(currentLettersGuessed, randomWord);
                    printLines(randomWord);
                }
                else
                {
                    bool right = false;                                                                                      //checking if Letters in the word
                    for (int i = 0; i < lengthOfWordToGuess; i++) { if (letterGuessed == randomWord[i]) { right = true; } }

                    if (right)
                    {
                        printHangman(amountOfTimesWrong);
                        currentLettersGuessed.Add(letterGuessed);
                        currentLettersRight = printWord(currentLettersGuessed, randomWord);            //for when user is right print the appropriate letters
                        Console.Write("\r\n");
                        printLines(randomWord);
                    }
                    else
                    {
                        amountOfTimesWrong++;
                        currentLettersGuessed.Add(letterGuessed);
                        printHangman(amountOfTimesWrong);
                        currentLettersRight = printWord(currentLettersGuessed, randomWord);          // for when the usder is wrong
                        Console.Write("\r\n");
                        printLines(randomWord);
                    }
                }
            }
            Console.WriteLine("\r\nGame is over! Thanks for playing :)");                              //end
        }
    }
}

