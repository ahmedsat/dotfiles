#include <raylib.h>

#define WIDTH 6 * SCALE

int main(void)
{
  SetConfigFlags(FLAG_WINDOW_RESIZABLE);

  InitWindow(800, 450, "Test");

  while (!WindowShouldClose())
  {
    BeginDrawing();
    ClearBackground(DARKGRAY);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}