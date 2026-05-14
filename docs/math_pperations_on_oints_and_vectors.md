
## Tools
- [Latex Editor Preview](https://latexeditor.lagrida.com/)
## Learning Resources
- [ ] [Hình học](https://www.scratchapixel.com/lessons/mathematics-physics-for-computer-graphics/geometry/points-vectors-and-normals.html)
- [ ] [Ma trận phối cảnh và phép chiếu trực giao ](https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/projection-matrix-introduction.html)


# Các phép toán trên điểm và vectơ 

## Độ dài của vector `length(a)`
Về mặt hình học thì nó cũng có thể được xem là một điểm trong không gian 3D: `(Vx, Vy, Vz)`. Nhưng trong linear algebra / graphics, người ta thường xem nó là:
- một vector xuất phát từ gốc tọa độ
- từ `(0, 0, 0)` tới `(Vx, Vy, Vz)`

nên công thức này thực chất đang tính khoảng cách từ gốc tọa độ đến điểm đó.
```math
\displaylines{
\left\|V\right\| = \sqrt{V_x^2 + V_y^2} \\ 
\left\|V\right\| = \sqrt{V_x^2 + V_y^2 + V_z^2}
}
```
## chuẩn hóa một vector `normalize(a)`

Chia vector cho độ dài của nó — kết quả là vector cùng hướng nhưng có độ dài bằng **1** (unit vector).

```math
\hat{V} = \frac{V}{\left\|V\right\|} = \left(\frac{V_x}{\left\|V\right\|},\ \frac{V_y}{\left\|V\right\|},\ \frac{V_z}{\left\|V\right\|}\right)
```

![normalize](https://www.scratchapixel.com/images/geometry/normalize.png)

## Tích vô hướng `dot(a, b)`

Nhân từng thành phần tương ứng rồi cộng lại — kết quả là một **số vô hướng** (scalar).

```math
A \cdot B = A_x B_x + A_y B_y + A_z B_z
```

Cũng bằng:

```math
A \cdot B = \left\|A\right\| \left\|B\right\| \cos\theta
```

Trong đó `θ` là góc giữa hai vector. Tính chất nhanh:
- `A · B > 0` → cùng hướng (góc nhọn)
- `A · B = 0` → vuông góc
- `A · B < 0` → ngược hướng (góc tù)

![dot product](https://www.scratchapixel.com/images/geometry/dotproduct.png)

## Tích có hướng `cross(a, b)`

Kết quả là một **vector vuông góc** với cả `A` và `B` (theo quy tắc bàn tay phải).

```math
C = A \times B = \begin{pmatrix} A_y B_z - A_z B_y \\ A_z B_x - A_x B_z \\ A_x B_y - A_y B_x \end{pmatrix}
```

Tính chất: **phản giao hoán** — `A × B = −(B × A)`

![cross product](https://www.scratchapixel.com/images/geometry/crossproduct.png)
![right-hand rule](https://www.scratchapixel.com/images/geometry/normalleftrighthand.png)
![right-hand rule 2](https://www.scratchapixel.com/images/geometry/normalleftrighthand2.png)

## Cộng vector `add(a, b)`

```math
A + B = (A_x + B_x,\ A_y + B_y,\ A_z + B_z)
```

## Trừ vector `subtract(a, b)`

```math
A - B = (A_x - B_x,\ A_y - B_y,\ A_z - B_z)
```

## Nhân vector với scalar `scale(a, r)`

```math
r \cdot V = (r \cdot V_x,\ r \cdot V_y,\ r \cdot V_z)
```

