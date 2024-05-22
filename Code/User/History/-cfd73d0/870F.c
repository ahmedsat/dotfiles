#include <raylib.h>

#define SCALE 150
#define WIDTH 9 * SCALE
#define HEIGHT 6 * SCALE

int main(void)
{
  SetConfigFlags(FLAG_WINDOW_RESIZABLE);

  InitWindow(WIDTH, HEIGHT, "Test");

  Camera3D camera = {0};
  camera.position = (Vector3){0.0f, 10.0f, 10.0f};
  camera.up = (Vector3){0, 1, 0};
  camera.fovy = 45;
  camera.projection = CAMERA_PERSPECTIVE;

  Vector3 cubePosition = {0.0f, 0.0f, 0.0f};

  while (!WindowShouldClose())
  {
    BeginDrawing();
    ClearBackground(DARKGRAY);

    EndDrawing();
  }

  CloseWindow();

  return 0;
}