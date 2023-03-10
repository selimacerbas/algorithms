#include <vector>

using namespace std;

class BinaryTree {
public:
  int value;
  BinaryTree *left;
  BinaryTree *right;

  BinaryTree(int value) {
    this->value = value;
    left = nullptr;
    right = nullptr;
  }
};

struct Level {
  BinaryTree *root;
  int depth;
};

int nodeDepths(BinaryTree *root) {
  auto depths {0};
  vector<Level> stack = {{root, 0}};
  
  while(stack.size() > 0)
  {
    BinaryTree *node = stack.back().root;
    int depth = stack.back().depth;
    stack.pop_back();

    if(node == nullptr)
      continue;

    depths += depth;
    stack.push_back(Level{node->left, depth +1});
    stack.push_back(Level{node->right, depth +1});
  }
  return depths;
}
