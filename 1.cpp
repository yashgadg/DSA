#include <iostream>
#include <cstring>
#include <cstdlib> 
#include <iomanip>
using namespace std;


struct Student
{
    int id;
    char name[50];
    float cgpa;
};


void addStudent(Student *&students, int &count);
void displayStudents(Student *students, int count);
void bubbleSortByName(Student *students, int count);
void selectionSortByCGPA(Student *students, int count, bool ascending);
int linearSearch(Student *students, int count, int id);
int binarySearch(Student *students, int count, int id);
void sortByID(Student *students, int count);

int main()
{
    Student *students = nullptr;
    int count = 0;
    int choice;

    do
    {
        cout << "\n===== STUDENT DATABASE MENU =====";
        cout << "\n1. Add Student";
        cout << "\n2. Display Students";
        cout << "\n3. Linear Search by ID";
        cout << "\n4. Binary Search by ID";
        cout << "\n5. Sort by Name (Bubble Sort)";
        cout << "\n6. Sort by CGPA (Selection Sort)";
        cout << "\n7. Exit";
        cout << "\nEnter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            addStudent(students, count);
            break;

        case 2:
            displayStudents(students, count);
            break;

        case 3:
        {
            int id;
            cout << "Enter ID to search: ";
            cin >> id;
            int index = linearSearch(students, count, id);
            if (index != -1)
                cout << "Found: ID=" << students[index].id
                     << ", Name=" << students[index].name
                     << ", CGPA=" << students[index].cgpa << endl;
            else
                cout << "Student not found.\n";
            break;
        }

        case 4:
        {
            if (count == 0)
            {
                cout << "No records available.\n";
                break;
            }
            sortByID(students, count); // must be sorted for binary search
            int id;
            cout << "Enter ID to search: ";
            cin >> id;
            int index = binarySearch(students, count, id);
            if (index != -1)
                cout << "Found: ID=" << students[index].id
                     << ", Name=" << students[index].name
                     << ", CGPA=" << students[index].cgpa << endl;
            else
                cout << "Student not found.\n";
            break;
        }

        case 5:
            bubbleSortByName(students, count);
            cout << "Sorted by name alphabetically.\n";
            break;

        case 6:
        {
            int order;
            cout << "1. Ascending  2. Descending\nEnter choice: ";
            cin >> order;
            selectionSortByCGPA(students, count, order == 1);
            cout << "Sorted by CGPA.\n";
            break;
        }

        case 7:
            cout << "Exiting...\n";
            break;

        default:
            cout << "Invalid choice.\n";
        }
    } while (choice != 7);

    free(students);
    return 0;
}


void addStudent(Student *&students, int &count)
{
    Student temp;
    cout << "Enter Student ID: ";
    cin >> temp.id;
    cout << "Enter Student Name: ";
    cin.ignore();
    cin.getline(temp.name, 50);
    cout << "Enter Student CGPA: ";
    cin >> temp.cgpa;

    
    students = (Student *)realloc(students, (count + 1) * sizeof(Student));
    if (students == nullptr)
    {
        cout << "Memory allocation failed.\n";
        exit(1);
    }

    students[count] = temp;
    count++;

    cout << "Student added successfully!\n";
}


void displayStudents(Student *students, int count)
{
    if (count == 0)
    {
        cout << "No students to display.\n";
        return;
    }

    cout << left << setw(10) << "ID" << setw(25) << "Name" << setw(10) << "CGPA" << endl;
    cout << "----------------------------------------------\n";
    for (int i = 0; i < count; i++)
    {
        cout << left << setw(10) << students[i].id
             << setw(25) << students[i].name
             << setw(10) << students[i].cgpa << endl;
    }
}


int linearSearch(Student *students, int count, int id)
{
    for (int i = 0; i < count; i++)
    {
        if (students[i].id == id)
            return i;
    }
    return -1;
}


void sortByID(Student *students, int count)
{
    for (int i = 0; i < count - 1; i++)
    {
        for (int j = 0; j < count - i - 1; j++)
        {
            if (students[j].id > students[j + 1].id)
            {
                Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }
}


int binarySearch(Student *students, int count, int id)
{
    int low = 0, high = count - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (students[mid].id == id)
            return mid;
        else if (students[mid].id < id)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}


void bubbleSortByName(Student *students, int count)
{
    for (int i = 0; i < count - 1; i++)
    {
        for (int j = 0; j < count - i - 1; j++)
        {
            if (strcmp(students[j].name, students[j + 1].name) > 0)
            {
                Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }
}


void selectionSortByCGPA(Student *students, int count, bool ascending)
{
    for (int i = 0; i < count - 1; i++)
    {
        int minOrMax = i;
        for (int j = i + 1; j < count; j++)
        {
            if (ascending ? (students[j].cgpa < students[minOrMax].cgpa)
                          : (students[j].cgpa > students[minOrMax].cgpa))
            {
                minOrMax = j;
            }
        }
        if (minOrMax != i)
        {
            Student temp = students[i];
            students[i] = students[minOrMax];
            students[minOrMax] = temp;
        }
    }
}