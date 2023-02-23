#include <stdio.h>
#include<malloc.h>
#include <stdlib.h>
#include<string.h>
#include<math.h>
double a = 0.43, b = 0.57; //tentmap parameter
double x_0 = 0.342781; //original x
double y_0 = 0.543981;//original y
#define iteration  300 //iteration number
double x_list[iteration];//store x
double y_list[iteration];//store y
long U_list[iteration + 1];//store fun(x,y)
int* Z_list;//store sym
int len = 0;//length of Z_list
int* h_list;//store iteration number of sym
int fun_list[10][10] = { {1,9,9,5,5,5,5,9,9,0},{2,2,2,2,1,0,3,3,3,3},{6,6,9,9,5,5,9,9,0,8},
								{6,6,1,9,5,5,9,0,8,8},{2,6,6,1,5,5,0,8,8,3},{2,2,2,2,0,1,3,3,3,3},
								{2,6,6,0,4,4,1,8,8,3},{6,6,0,7,4,4,7,1,8,8},{6,0,7,7,4,4,7,7,1,8},
								{0,7,7,4,4,4,4,7,7,1} }; //二次映射数组
// 二次映射
int fun(double x, double y) {
	int i = 0, j = 0;
	while (i < 10) {
		j = 0;
		while (j < 10) {
			float i1 = i / 10.0;
			float i2 = (i + 1.0) / 10.0;
			float j1 = j / 10.0;
			float j2 = (j + 1.0) / 10.0;
			if (x >= i1 && x <= i2 && y >= j1 && y <= j2) {
				//printf("i1=%f,i2=%f,j1=%f,j2=%f,", i1, i2, j1, j2);
				//printf("U_list[%d][%d]=%d\n", i, j, fun_list[i][j]);
				return fun_list[i][j];
			}
			j++;
		}
		i++;
	}
	return -1;
}

//tent map
void two_tentmap(double x0, double y0, double a, double b) {
	double x = x_0, y = y_0;
	int i = 1;
	U_list[0] = -1;
	while (i <= iteration) {
		if (x >= 0 && x < a && y >= 0 && y < b) {
			x = x / a;
			y = y / b;
		}
		else if (x >= a && x <= 1 && y >= 0 && y < b) {
			x = (1.0 - x) / (1.0 - a);
			y = y / b;
		}
		else if (x >= 0 && x < a && y >= b && y <= 1) {
			x = x / a;
			y = (1.0 - y) / (1.0 - b);
		}
		else if (x >= a && x <= 1 && y >= b && y <= 1) {
			x = (1.0 - x) / (1.0 - a);
			y = (1.0 - y) / (1.0 - b);
		}
		x_list[i] = x;
		y_list[i] = y;
		//printf("x=%.16lf,y=%.16lf\n", x, y);
		int N = fun(x, y);
		U_list[i] = N;
		//printf("U_list[i]=%d,", U_list[i]);
		i++;
	}
}

//convert sym into array format
void sym_list(int a) {
	//len = (a == 0 ? 1 : (int)log10(abs(a)) + 1);
	int k=a;
	while(k>=1){
		k=k/10;
		len++;
	}
	Z_list = (int*)malloc(sizeof(int) * len);
	if (Z_list == NULL) {
		printf("Z_list malloc failed！\n");
	}
	else {
		int j = 0;
		while (a >= 1) {
			int b = a % 10;
			a = a / 10;
			*(Z_list + len - 1 - j) = b;
			j++;
		}
	}

}

// find proper iteration number
void found_hlist() {
	h_list = (int*)malloc(sizeof(int) * len);
	if (h_list == NULL) {
		printf("h_list malloc failed！\n");
	}
	else {
		int i = 0;
		for (int z = 0; z < len; z++) {
			for (int u = 0; u <= iteration; u++) {
				if (Z_list[z] == U_list[u]) {
					*(h_list + i) = u;
					i++;
					break;
				}
			}
		}
	}
}

int found_value(int* h_list, int len) {
	int value = 0;
	for (int i = 0; i < len; i++) {
		for (int j = 1; j <= iteration; j++) {
			if (h_list[i] == j) {
				value = value * 10 + U_list[j];
			}
		}

	}
	return value;
}

int solve(int sym) {
	two_tentmap(x_0, y_0, a, b);
	sym_list(sym);
	found_hlist();
	return found_value(h_list, len);
}

void Bogus() {
	printf("Bogus\n");
}
void Foo(int a) {
	printf("Foo,sym_var=%d\n",a);
}
int main(int argc, char** argv) {// call solve() function
	int value0=solve(0);
  printf("%d",value0);
}
