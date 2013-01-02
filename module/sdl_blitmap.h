typedef struct
{
    Uint8 *src;
    int src_w, src_h;
    int src_pitch;
    int src_skip;
    Uint8 *dst;
    int dst_w, dst_h;
    int dst_pitch;
    int dst_skip;
    SDL_PixelFormat *src_fmt;
    SDL_PixelFormat *dst_fmt;
    Uint8 *table;
    int flags;
    Uint32 colorkey;
    Uint8 r, g, b, a;
} SDL_BlitInfo;

typedef struct SDL_BlitMap
{
    SDL_Surface *dst;
    int identity;
    SDL_blit blit;
    void *data;
    SDL_BlitInfo info;

    /* the version count matches the destination; mismatch indicates
       an invalid mapping */
    Uint32 dst_palette_version;
    Uint32 src_palette_version;
} SDL_BlitMap;
