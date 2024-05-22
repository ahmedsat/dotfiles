#include <raylib.h>

#define SCALE 150
#define WIDTH 9 * SCALE
#define HEIGHT 6 * SCALE

#define CENTER \
  (Vector3) { 0.0f, 0.0f, 0.0f }

int main(void)
{
  SetConfigFlags(FLAG_WINDOW_RESIZABLE);

  InitWindow(WIDTH, HEIGHT, "Test");

  Camera3D camera = {0};
  camera.position = (Vector3){1.0f, 100.0f, 0.0f};
  camera.up = (Vector3){0, 1, 0};
  camera.fovy = 45;
  camera.projection = CAMERA_PERSPECTIVE;

  Vector3 particle = {50, 50, 50};

  while (!WindowShouldClose())
  {
    BeginDrawing();

    {
      ClearBackground(BLACK);

      BeginMode3D(camera);

      {
        DrawSphere(CENTER, 1, WHITE);
        DrawSphere(particle, 1, GREEN);
      }

      EndMode3D();

      DrawFPS(10, 10);
    }

    EndDrawing();
  }

  CloseWindow();

  return 0;
}