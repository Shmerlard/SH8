/*

const unsigned int PCin = 1;
const unsigned int PCout = 2;
const unsigned int PCinc = 3;

enum ctrlLines {
    PCin,
    PCout,
    PCinc,
    RFin,
    RFout,
    DSTsel
};
*/
#include "sh8lib.h"
#include <string.h>
#include <stdio.h>
#define PCin  = 0b00;
#define PCout = 0b10;

char ctrlLines[CTRLSIZE][10] = {
        "PCin",
        "PCout",
        "PCinc",
        "RFin",
        "RFout",
        "DSTsel",
        "IRin",
        "IRout"
};

int ctrl_lines_to_bin(char* input[],int length) {
    //int length1 = sizeof(input[0])/sizeof(input[0][0]);
    //printf("%d\n",length1);
    int output = 0;
    
    for(int i = 0;i < length; i++){
        for(int j = 0; j < CTRLSIZE;j++){
            if(strcmp(input[i],ctrlLines[j]) ==0){
                output = output + (1 << j);
                //break;
            }
        }
    }
    
    return output;
}
