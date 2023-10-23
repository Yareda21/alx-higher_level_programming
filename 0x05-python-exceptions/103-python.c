#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;
	Py_ssize_t size;
	Py_ssize_t alloc;
	Py_ssize_t y;
	const char *type;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("\t[ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (y = 0; y < size; y++)
	{
		type = list->ob_item[y]->ob_type->tp_name;
		printf("Element %ld: %s\n", y, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[y]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[y]);
	}
}

/**
 * print_python_bytes -
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t z;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("\t[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("\tsize: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("\ttrying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("\tfirst %ld bytes: ", size);
	for (z = 0; z < size; z++)
	{
		printf("%02hhx", bytes->ob_sval[z]);
		if (z == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj = (PyFloatObject *)p;
	char *buffer = NULL;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("\t[ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("\tvalue: %s\n", buffer);
	PyMem_Free(buffer);
}

