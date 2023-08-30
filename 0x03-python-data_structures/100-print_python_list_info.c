#include <Python.h>
#include <stdio.h>
#include <object.h>

/**
 *print_python_list_info - prints python lists
 *@p:pyobject
 *Return: no return
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int b;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %lb\n", list->allocated);
	for (b = 0; b < size; b++)
		printf("Element %b: %s\n", b, Py_TYPE(list->ob_item[b])->tp_name);
}
