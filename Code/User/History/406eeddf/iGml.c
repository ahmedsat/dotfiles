#define NOB_IMPLEMENTATION
#include "./include/nob.h"

void cc(Nob_Cmd *cmd){
    nob_cmd_append(cmd, "cc", "-o" , "./build/app");
}

void cFlags(Nob_Cmd *cmd){
    nob_cmd_append(cmd,"-Wall","-Wextra","-pedantic");
}

void include(Nob_Cmd *cmd){
    nob_cmd_append(cmd,"-I")
}

int main(int argc, char **argv){
    NOB_GO_REBUILD_URSELF(argc, argv);

    Nob_Cmd cmd = {0};
    cc(&cmd);
    cFlags(&cmd);
    nob_cmd_append(&cmd, "./src/main.c");

    if (!nob_cmd_run_sync(cmd)) return 1;

    return 0;

}