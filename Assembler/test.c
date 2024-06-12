#include <stdio.h>
#include <string.h>
#include "sh8lib.h"
//#define CTRLSIZE 8
/*
char *ctrlLines[CTRLSIZE] = {
        "PCin",
        "PCout",
        "PCinc",
        "RFin",
        "RFout",
        "DSTsel",
        "IRin",
        "IRout"
};
int ctrl_lines_to_bin(char *input[],int length);

*/

int main() {
   
    char input[][10] = {
        "PCinc","RFout"
    };
    int length = 2;

    int output = ctrl_lines_to_bin(**input, &length);
    printf("%d\n", output);
    return 0;
}
/*
int ctrl_lines_to_bin(char *input[],int length) {
    int output = 0;
    for(int i = 0;i < length; i++){
        for(int j = 0; j<CTRLSIZE;j++){
            if(input[i] == ctrlLines[j]){
                output = output + (1 << j);
                break;
            }
        }
    }
    return output;
}

*/