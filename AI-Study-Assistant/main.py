from ai_review import review_code

code = """
#include <stdio.h>
int main(){
printf("hello");
}
"""

print(review_code(code))