#include <raylib.h>

int main(void)
{
  InitWindow(800, 450, "raylib [core] example - basic window");

  while (!WindowShouldClose())
  {
    BeginDrawing();
    ClearBackground(GRAY);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}