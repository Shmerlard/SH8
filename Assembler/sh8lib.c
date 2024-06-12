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

//const unsigned char CTRLSIZE = 8;

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

int ctrl_lines_to_bin(char** pinput,int* plength) {
    int output = 0;
    return 3;
    /*
    for(int i = 0;i < *plength; i++){
        for(int j = 0; j<CTRLSIZE;j++){
            if(input[i] == ctrlLines[j]){
                output = output + (1 << j);
                //break;
            }
        }
    }
    */
    //return output;
}
