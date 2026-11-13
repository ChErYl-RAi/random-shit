/*
sandsim.c
by cheryl
yeags. meow.
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include "raylib.h"
struct grain{
    int x;
    int y;
};
int main(){
    srand((unsigned int)time(NULL));
    int grnNum = 0;
    int waNum = 0;
    int walNum = 0;
    static struct grain allgrains[122500];
    static struct grain allwawa[122500];
    static struct grain allwall[122500];
    const int screenWidth = 350;
    const int screenHeight = 350;
    InitWindow(screenWidth, screenHeight, "sand");
    //SetTargetFPS(60);
    static int grid[350][350] = {0};
    while (!WindowShouldClose())
    {
        for (size_t i = 0; i < grnNum; i++){
            grid[allgrains[i].x][allgrains[i].y]=1;
        }
        for (size_t i = 0; i < waNum; i++){
            grid[allwawa[i].x][allwawa[i].y]=1;
        }
        for (size_t i = 0; i < walNum; i++){
            grid[allwall[i].x][allwall[i].y]=1;
        }
        if (GetTouchPointCount()>0){
            Vector2 mp = GetTouchPosition(0);
            bool cango=true;
            for (size_t i = 0; i < grnNum; i++){
                if (allgrains[i].y==mp.y && allgrains[i].x==mp.x){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x;
                tmpggrain.y=mp.y;
                allgrains[grnNum] = tmpggrain;
                grnNum++;
            }
        }
        if (IsMouseButtonDown(0)){
            Vector2 mp = GetMousePosition();
            bool cango=true;
            for (size_t i = 0; i < grnNum; i++){
                if (allgrains[i].y==mp.y && allgrains[i].x==mp.x){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x;
                tmpggrain.y=mp.y;
                allgrains[grnNum] = tmpggrain;
                grnNum++;
            }
        }
        if (IsMouseButtonDown(1)){
            Vector2 mp = GetMousePosition();
            bool cango=true;
            for (size_t i = 0; i < waNum; i++){
                if (allwawa[i].y==mp.y && allwawa[i].x==mp.x){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x;
                tmpggrain.y=mp.y;
                allwawa[waNum] = tmpggrain;
                waNum++;
            }
        }

        
        if (IsMouseButtonDown(2)){
            Vector2 mp = GetMousePosition();
            //5
            bool cango=true;
            for (size_t i = 0; i < walNum; i++){
                if (allwall[i].y==mp.y && allwall[i].x==mp.x){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x;
                tmpggrain.y=mp.y;
                allwall[walNum] = tmpggrain;
                walNum++;
            }
            //1
            cango=true;
            for (size_t i = 0; i < walNum; i++){
                if (allwall[i].y==mp.y-1 && allwall[i].x==mp.x-1){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x-1;
                tmpggrain.y=mp.y-1;
                allwall[walNum] = tmpggrain;
                walNum++;
            }
            //3
            cango=true;
            for (size_t i = 0; i < walNum; i++){
                if (allwall[i].y==mp.y-1 && allwall[i].x==mp.x+1){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x-1;
                tmpggrain.y=mp.y+1;
                allwall[walNum] = tmpggrain;
                walNum++;
            }
            //7
            cango=true;
            for (size_t i = 0; i < walNum; i++){
                if (allwall[i].y==mp.y+1 && allwall[i].x==mp.x-1){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x+1;
                tmpggrain.y=mp.y-1;
                allwall[walNum] = tmpggrain;
                walNum++;
            }
            //9
            cango=true;
            for (size_t i = 0; i < walNum; i++){
                if (allwall[i].y==mp.y+1 && allwall[i].x==mp.x+1){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x+1;
                tmpggrain.y=mp.y+1;
                allwall[walNum] = tmpggrain;
                walNum++;
            }
            
            //1
            cango=true;
            for (size_t i = 0; i < walNum; i++){
                if (allwall[i].y==mp.y && allwall[i].x==mp.x-1){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x-1;
                tmpggrain.y=mp.y;
                allwall[walNum] = tmpggrain;
                walNum++;
            }
            //3
            cango=true;
            for (size_t i = 0; i < walNum; i++){
                if (allwall[i].y==mp.y && allwall[i].x==mp.x+1){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x-1;
                tmpggrain.y=mp.y;
                allwall[walNum] = tmpggrain;
                walNum++;
            }
            //7
            cango=true;
            for (size_t i = 0; i < walNum; i++){
                if (allwall[i].y==mp.y-1 && allwall[i].x==mp.x){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x;
                tmpggrain.y=mp.y-1;
                allwall[walNum] = tmpggrain;
                walNum++;
            }
            //9
            cango=true;
            for (size_t i = 0; i < walNum; i++){
                if (allwall[i].y==mp.y+1 && allwall[i].x==mp.x){
                    cango=false;
                }
            }
            if (cango){
                struct grain tmpggrain;
                tmpggrain.x=mp.x;
                tmpggrain.y=mp.y+1;
                allwall[walNum] = tmpggrain;
                walNum++;
            }
        }

        for (size_t i = 0; i < grnNum; i++)
        {
            if (allgrains[i].y<349){
                bool cango=true;
                if (grid[allgrains[i].x][allgrains[i].y+1]){
                    cango=false;
                }
                if (cango){
                    grid[allgrains[i].x][allgrains[i].y]=0;
                    allgrains[i].y++;
                }else{
                    if (rand() % 2){
                        bool cang2=true;
                        if (grid[allgrains[i].x][allgrains[i].y+1]){
                            cango=false;
                        }
                        if (!(allgrains[i].y<349)){
                            cango=false;
                        }
                        if (grid[allgrains[i].x+1][allgrains[i].y+1]){
                            cang2=false;
                        }
                        if (cang2){
                            grid[allgrains[i].x][allgrains[i].y]=0;
                            allgrains[i].y++;
                            allgrains[i].x++;
                        }
                    }else{
                        bool cang2=true;
                        if (grid[allgrains[i].x][allgrains[i].y+1]){
                            cango=false;
                        }
                        if (!(allgrains[i].y<349)){
                            cango=false;
                        }
                        if (grid[allgrains[i].x-1][allgrains[i].y+1]){
                            cang2=false;
                        }
                        if (cang2){
                            grid[allgrains[i].x][allgrains[i].y]=0;
                            allgrains[i].y++;
                            allgrains[i].x-=1;
                        }
                    }
                    
                }
            }
        }

        for (size_t i = 0; i < waNum; i++)
        {
            bool cango=true;
            if (grid[allwawa[i].x][allwawa[i].y+1]){
                cango=false;
            }
            if (!(allwawa[i].y<349)){
                cango=false;
            }
            if (cango){
                grid[allwawa[i].x][allwawa[i].y]=0;
                allwawa[i].y++;
            }else{
                if (rand() % 2){
                    bool cang2=true;
                    if (allwawa[i].x == 0){
                        cang2=false;
                    }
                    if (allwawa[i].x == 359){
                        cang2=false;
                    }
                    if (grid[allwawa[i].x+1][allwawa[i].y]){
                        cang2=false;
                    }
                    if (cang2){
                        grid[allwawa[i].x][allwawa[i].y]=0;
                        allwawa[i].x++;
                        if (allwawa[i].x>349){
                            allwawa[i].x-=350;
                        }
                    }
                }else{
                    bool cang2=true;
                    if (allwawa[i].x == 0){
                        cang2=false;
                    }
                    if (allwawa[i].x == 359){
                        cang2=false;
                    }
                    if (grid[allwawa[i].x-1][allwawa[i].y]){
                        cang2=false;
                    }
                    if (cang2){
                        grid[allwawa[i].x][allwawa[i].y]=0;
                        allwawa[i].x-=1;
                        if (allwawa[i].x<0){
                            allwawa[i].x+=350;
                        }
                    }
                }
            }
        }

        BeginDrawing();
            ClearBackground(BLACK);
            for (size_t i = 0; i < grnNum; i++)
            {
                DrawPixel(allgrains[i].x,allgrains[i].y,YELLOW);
            }

            for (size_t i = 0; i < waNum; i++)
            {
                DrawPixel(allwawa[i].x,allwawa[i].y,BLUE);
            }

            for (size_t i = 0; i < walNum; i++)
            {
                DrawPixel(allwall[i].x,allwall[i].y,GRAY);
            }
        EndDrawing();
    }
    CloseWindow();
}