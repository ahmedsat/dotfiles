#include <raylib.h>

int main(void)
{
  SetConfigFlags()
      InitWindow(800, 450, "App");

  while (!WindowShouldClose())
  {
    BeginDrawing();
    ClearBackground(GRAY);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}