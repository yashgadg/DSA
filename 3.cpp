#include <iostream>
using namespace std;

#define SIZE 5 

class CircularQueue
{
private:
    int items[SIZE];
    int front, rear;

public:
    CircularQueue()
    {
        front = -1;
        rear = -1;
    }

    
    bool isFull()
    {
        return (front == 0 && rear == SIZE - 1) || (front == rear + 1);
    }

    
    bool isEmpty()
    {
        return (front == -1);
    }


    void enqueue(int element)
    {
        if (isFull())
        {
            cout << "Queue is FULL! Cannot insert " << element << endl;
            return;
        }

        if (front == -1) 
            front = 0;

        rear = (rear + 1) % SIZE;
        items[rear] = element;
        cout << "Inserted: " << element << endl;
    }

    
    void dequeue()
    {
        if (isEmpty())
        {
            cout << "Queue is EMPTY! Cannot dequeue.\n";
            return;
        }

        cout << "Deleted: " << items[front] << endl;

        if (front == rear)
        { 
            front = -1;
            rear = -1;
        }
        else
        {
            front = (front + 1) % SIZE;
        }
    }

    
    void display()
    {
        if (isEmpty())
        {
            cout << "Queue is EMPTY!\n";
            return;
        }

        cout << "Queue elements: ";
        int i = front;
        while (true)
        {
            cout << items[i] << " ";
            if (i == rear)
                break;
            i = (i + 1) % SIZE;
        }
        cout << endl;
    }
};


int main()
{
    CircularQueue q;
    int choice, value;

    do
    {
        cout << "\n===== Circular Queue Menu =====\n";
        cout << "1. Enqueue (Insert)\n";
        cout << "2. Dequeue (Delete)\n";
        cout << "3. Display Queue\n";
        cout << "0. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "Enter value to insert: ";
            cin >> value;
            q.enqueue(value);
            break;

        case 2:
            q.dequeue();
            break;

        case 3:
            q.display();
            break;

        case 0:
            cout << "Exiting program...\n";
            break;

        default:
            cout << "Invalid choice! Try again.\n";
        }

    } while (choice != 0);

    return 0;
}
