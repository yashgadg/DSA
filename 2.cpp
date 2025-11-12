#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
using namespace std;


struct Node {
    char data;
    Node* next;
};


class Stack {
private:
    Node* top;
public:
    Stack() { top = nullptr; }

    bool isEmpty() {
        return top == nullptr;
    }

    void push(char value) {
        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = top;
        top = newNode;
    }

    char pop() {
        if (isEmpty()) {
            return '\0';
        }
        char value = top->data;
        Node* temp = top;
        top = top->next;
        delete temp;
        return value;
    }

    char peek() {
        if (isEmpty()) return '\0';
        return top->data;
    }

    void clear() {
        while (!isEmpty()) pop();
    }
};


int precedence(char op) {
    switch (op) {
        case '^': return 3;
        case '*':
        case '/': return 2;
        case '+':
        case '-': return 1;
        default:  return 0;
    }
}


bool isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^');
}


string infixToPostfix(const string& infix) {
    Stack s;
    string postfix = "";

    for (char ch : infix) {
        if (isspace(ch)) continue;  

        if (isalnum(ch)) {
            postfix += ch; 
        }
        else if (ch == '(') {
            s.push(ch);
        }
        else if (ch == ')') {
            while (!s.isEmpty() && s.peek() != '(') {
                postfix += s.pop();
            }
            s.pop(); 
        }
        else if (isOperator(ch)) {
            while (!s.isEmpty() && precedence(s.peek()) >= precedence(ch)) {
                postfix += s.pop();
            }
            s.push(ch);
        }
    }

    while (!s.isEmpty()) {
        postfix += s.pop();
    }

    return postfix;
}

string infixToPrefix(string infix) {
    Stack s;
    string prefix = "";


    reverse(infix.begin(), infix.end());


    for (char &ch : infix) {
        if (ch == '(') ch = ')';
        else if (ch == ')') ch = '(';
    }

    
    string revPostfix = infixToPostfix(infix);

    
    reverse(revPostfix.begin(), revPostfix.end());

    return revPostfix;
}
int main() {
    string infix;

    cout << "Enter an infix expression: ";
    getline(cin, infix);

    string postfix = infixToPostfix(infix);
    string prefix = infixToPrefix(infix);

    cout << "\nInfix Expression:   " << infix;
    cout << "\nPostfix Expression: " << postfix;
    cout << "\nPrefix Expression:  " << prefix << endl;

    return 0;
}

