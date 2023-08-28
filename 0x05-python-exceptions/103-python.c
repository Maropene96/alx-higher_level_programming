#include <stdio.h>
#include <python.h>
/**
 * print_python_float - prints python floats objects
 * @p: Python Object
 * Return: no return
 */
void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	setbuf(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}
/**
 * print_python_bytes - prints Python Bytes Object
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, t = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (t < size + 1 && t < 10)
	{
		printf(" %02hhx", string[t]);
		t++;
	}
	printf("\n");
}
/**
 * print_python_list - ptints the data of a python lists
 * @p: python Object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int t = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (t < size)
		{
			item = PyList_GET_ITEM(p, t);
			printf("Element %d: %s\n", t, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			t++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
