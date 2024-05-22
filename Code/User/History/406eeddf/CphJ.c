#define NOB_IMPLEMENTATION
#include "./include/nob.h"

void cc(Nob_Cmd *cmd)
{
    nob_cmd_append(cmd, "cc", "-o", "./build/app");
}

void include(Nob_Cmd *cmd)
{
    nob_cmd_append(cmd, "-Iexternal/raylib-5.0/include/");
}

void cFlags(Nob_Cmd *cmd)
{
    nob_cmd_append(cmd, "-Wall", "-Wextra", "-pedantic");
    include(cmd);
}

void ld(Nob_Cmd *cmd)
{
    nob_cmd_append(cmd, "external/raylib-5.0/lib/libraylib.a");
}

int main(int argc, char **argv)
{
    NOB_GO_REBUILD_URSELF(argc, argv);

    Nob_Cmd cmd = {0};
    cc(&cmd);
    cFlags(&cmd);
    nob_cmd_append(&cmd, "./src/main.c");
    ld(&cmd);

    if (!nob_cmd_run_sync(cmd))
        return 1;

    return 0;
}