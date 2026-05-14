def main():
    imp = input("Expression: ").strip()
    answer = interpreter(imp)

    print(f"{answer:.1f}")


def interpreter(cal):
    x, y, z = cal.split()


    new_x = float(x)
    new_z = float(z);


    match y:
        case "+":
            return new_x + new_z
        case "-":
            return new_x - new_z
        case "*":
            return new_x * new_z
        case "/":
            return new_x / new_z
        
if __name__ == "__main__":
    main()