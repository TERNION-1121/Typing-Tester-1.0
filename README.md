<h1 align = "center"> ⌨ Typing-Tester-1.0 💻</h1>

 A repository for Typing Tester 1.0: A basic python program to check `Typing Speed` in words per minute **(WPM)** and `Typing Accuracy` in percent **(%)**.
 

 ###### Credits
 The idea for Typing-Tester-1.0 was given by [Legendary3995](https://github.com/Legendary3995), You all can find him on Discord `@Legendary#3995`. Don't forget to DM him a Thank You for providing this amazing idea!
 
 
## About Typing Tester 1.0
This program provides the user a `sentence` string, whose data can be changed as per individual will. The user has to press `Enter`, and then start typing the `sentence` string that is displayed. After typing, the user has to press `Enter` to see the final results i.e. **Typing Speed** and **Typing Accuracy**.


## How Typing Speed and Accuracy are calculated?


**Typing Speed** `(Standard Gross WPM)` is calculated by the number of words typed per minute i.e. `total number of words typed / time taken in minutes`; where each individual word consists of 5 keystrokes/characters. 

Following the given above, the `characters` entered by the user (length of the input string `words`) is divided by 5. Further it's divided by time taken in minutes.

<hr>


**Typing Accuracy** `(Accuracy)`, in this program, is calculated by `(correct words / total words typed) * 100`; rather than `(correct characters / total characters typed) * 100`.


<hr>


###### Standard Net WPM

`Standard Net WPM` is calculated by multiplying `Standard Gross WPM` by `Accuracy`. For example:
- Standard Gross WPM: `76 WPM`
- Accuracy: `93.75 %`
- Then, Standard Net WPM: (76 * 93.75) / 100
                     i.e. `71.25 WPM`

<hr>

Refer to this [Document](https://www.peoplogicaskills.com/wp-content/uploads/2016/06/Typing-and-Data-Entry-Calculation.pdf) for comprehensive definitions, regarding the terms mentioned above.


To verify the results shown at the end of the program, un-comment the lines given at the end of the `typing_test()` function to see the values used to calculate the corresponding results.




<hr>

###### To Use the Program
**Download** and **Open** the `main.exe` file provided in the repository, You would be able to use to program then.
