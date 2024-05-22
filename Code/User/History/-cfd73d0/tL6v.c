#include <raylib.h>

#define SCALE 150
#define WIDTH 9 * SCALE
#define HEIGHT 6 * SCALE

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