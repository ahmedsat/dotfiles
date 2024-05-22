#define NOB_IMPLEMENTATION
#include "./include/nob.h"

void cc(Nob_Cmd *cmd){
    nob_cmd_append(cmd, "cc", "-o" , "./build/app")
}

int main(int argc, char **argv){
    NOB_GO_REBUILD_URSELF(argc, argv);

    Nob_Cmd cmd = {0};
    cc(&cmd)
    nob_cmd_append(&cmd, "./src/main.c");

    if (!nob_cmd_run_sync(cmd)) return 1;

    return 0;

}