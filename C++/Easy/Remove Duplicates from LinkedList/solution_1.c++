using namespace std;

class LinkedList
{
    public:
    int value;
    LinkedList *next {nullptr};

    //Constructor
    LinkedList(int value)
    {
        this->value = value;
    }
};

LinkedList *removeDuplicatesFromLinkedList(LinkedList *LinkedList);

LinkedList *removeDuplicatesFromLinkedList(LinkedList *linkedList)
{
    auto currentNode {linkedList};

    while(currentNode != nullptr)
    {
        auto nextNode {currentNode->next};

        while(nextNode != nullptr && nextNode->value == currentNode->value)
        {
            nextNode = nextNode->next;
        }

        currentNode->next = nextNode;
        currentNode = nextNode;
    }

    return linkedList;

}
