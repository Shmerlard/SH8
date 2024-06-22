#include <stdio.h>
#include <string.h>
#include "sh8lib.h"



int main() {
   
    char* input[] = {
        "PCinc","RFout","PCin"
    };

  
    int output = ctrl_lines_to_bin(input, 3);
    printf("%d\n",  output);
    return 0;
}