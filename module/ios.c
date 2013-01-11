#include <Python.h>
#include <SDL/SDL.h>
#include <SDL/SDL_keyboard.h>

static PyObject *ios_show_keyboard(PyObject *self, PyObject *args)
{
  int result = SDL_ShowScreenKeyboard(SDL_VideoWindow);
  return Py_BuildValue("i", result);
}

static PyObject *ios_hide_keyboard(PyObject *self, PyObject *args)
{
  int result = SDL_HideScreenKeyboard(SDL_VideoWindow);
  return Py_BuildValue("i", result);
}

static PyMethodDef IosMethods[] = {
  {"show_keyboard", ios_show_keyboard, METH_VARARGS, "Show the screen keyboard"},
  {"hide_keyboard", ios_hide_keyboard, METH_VARARGS, "Hide the screen keyboard"},
  {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initios(void)
{
  (void) Py_InitModule("ios", IosMethods);
}
