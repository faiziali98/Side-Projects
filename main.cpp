
#include <iostream>

using namespace std;

struct node {
    void* val;
    node* next;
};

template <class T>
class List {

private:
    node *head, *tail;

public:
    void printval(void *v){
        cout<<*((T *)v)<<endl;
    }
    
    List()
    {
        head = NULL;
        tail = NULL;
    }
    List(void* x)
    {

        head = NULL;
        tail = NULL;
        node* temp = new node;
        temp->val = x;
        temp->next = NULL;
        if (head == NULL) {
            head = temp;
            tail = temp;
            temp = NULL;
        }
        else {
            tail->next = temp;
            tail = temp;
        }
    }
    
    List(const List &hello) {
        head=NULL;
        tail=NULL;
        
        if (hello.head!=NULL){
            head=NULL;
            tail=NULL;
            node *a = hello.get_head();
            while (a!=NULL)
            {
                insert_at_tail(a->val);
                printval(a->val);
                a = a->next;
            }
        }
    }
    
    void insert_at_head(void* x)
    {

        node* temp = new node;
        temp->val = x;
        temp->next = head;
        head = temp;
    }

    void insert_at_tail(void* x)
    {
        node* temp = new node;
        temp->val = x;
        temp->next = NULL;
        if (head == NULL) {
            head = temp;
            tail = temp;
            temp = NULL;
        }
        else {
            tail->next = temp;
            tail = temp;
        }
    }

    void insert_sorted(void* x){ //assume the list is sorted based on pointer values
        if (head!=NULL){
            node *a = head;
            node *c = NULL;
            while (a->val<=x){
                if (a!=tail){
                    c=a;
                    a=a->next;
                }else{
                    insert_at_tail(x);
                    a = NULL;
                    break;
                }
            }
            
            if (a==head){
                insert_at_head(x);
            }
            else if (a!=NULL){
                node *temp = new node;
                temp->val = x;
                temp->next = a;
                c->next = temp;
            }
        }
        else{
            insert_at_head(x);
        }
    }

    void delete_head()
    {
        node* temp;
        temp = head;
        if (head == NULL) {
            return;
        }
        else if (head->next == NULL) {
            head = NULL;
        }
        else if (head->next != NULL) {
            head = head->next;
        }
        delete temp;
    }
    void delete_tail()
    {
        node* now = new node;
        node* before = new node;
        now = head;
        before = NULL;
        if (tail == NULL) {
            return;
        }

        else {
            while (now->next != NULL) {
                before = now;
                now = now->next;
            }

            tail = before;
            before->next = NULL;
        }
        delete now;
    }

    void delete_ele(void* del)
    {
        node* arr = head;
        node* prev = arr->next;
        if (arr->val == del) {

            arr = prev;
            delete arr;
            prev = arr->next;
        }
        while (prev != NULL) {
            if (prev->val == del) {
                arr->next = prev->next;
                delete prev;
                prev = arr->next;
            }
            else {
                arr = prev;
                prev = prev->next;
            }
        }
    }

    node* get_ele(void* element)
    {
        node* here = head;

        while (here != NULL && here->val != element) {
            here = here->next;
        }
        if (here->val == element) {
            cout << "Yaay" << endl;
            return here;
        }
        else {
            cout << "Not found" << endl;
        }
    }

    node* get_head() const
    {
        cout << head << endl;
        return head;
    }

    node* get_tail()
    {
        tail = head;
        while (tail->next != NULL) {
            tail = tail->next;
        }
        return tail;
    }
    void reverse_me()
    {
        if (head == NULL) {
            return;
        }

        node *before = NULL, *now = NULL, *next = NULL;
        now = head;
        while (now != NULL) {
            next = now->next;
            now->next = before;
            before = now;
            now = next;
        }
        head = before;
    }
    
    void print()
    {
        node* temp = new node;
        temp = head;
        cout << "The list is as follows: " << endl;
        while (temp != NULL) {
            cout << *(T*)(temp->val);
            temp = temp->next;
            cout << " ";
        }
        cout << endl;
    }
};

int main()
{
    int num;
    cin >> num;
    void* p;
    p = &num;
    List <int>wow(p);
    wow.print();
    cout << endl;
    int z = 7;
    wow.insert_at_head(&z);
    wow.print();
    cout << endl;
    int y;
    y = 10;
    wow.insert_at_tail(&y);
    int u;
    u = 11;
    int k = 23;
    wow.insert_at_tail(&u);
    wow.insert_sorted(&u);
    wow.print();
    cout << endl;
    wow.reverse_me();
    wow.get_head();
    wow.get_tail();
    wow.print();
    cout << endl;
    // wow.delete_head();
    //wow.print();
    // wow.delete_tail();
    //  wow.print();
    //  wow.get_ele(&y);
    wow.delete_ele(&y);
    wow.print();
    List <int>then(wow);
    then.print();

    return 0;
}