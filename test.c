#include <stdio.h>

// 코드 1.4 배열에 중복 요소가 있는지 검사

int has_duplicate_elem(int A[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (A[i] == A[j]) // 중복 요소 있음
                return 1;    // TRUE 반환
        }
    }
    return 0; // 중복 요소가 없음. FALSE 반환
}

// 테스트 프로그램
void main()
{
    int a[8] = { 32, 14, 5, 17, 23, 9, 11, 4 };
    int b[8] = { 32, 14, 5, 17, 23, 14, 11, 4 };

    printf("A: 중복된 요소 %s\n", has_duplicate_elem(a, 8) ? "있음" : "없음");
    printf("B: 중복된 요소 %s\n", has_duplicate_elem(b, 8) ? "있음" : "없음");
}