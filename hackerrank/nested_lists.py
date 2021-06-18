"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints
2 <= N <= 5
There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, 
order their names alphabetically and print each one on a new line.

Sample Input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output
Berry
Harry

Other Example
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21

Sample Output
Beria
Harsh

Explanation
There are  students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, 
so we order their names alphabetically and print each name on a new line.
"""

if __name__ == "__main__":
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
    
    sl = sorted(set(scores))[1]

    names = [name for name, score in students if score == sl]

    print("\n".join(sorted(names)))

    
        



