import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Identifier {
    private String name;
    private String type;

    public Identifier(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }
}

class SymbolTableManager {
    private Map<String, Identifier> table = new HashMap<>();

    public void insert(Identifier identifier) {
        table.put(identifier.getName(), identifier);
    }

    public Identifier lookup(String name) {
        return table.get(name);
    }

    public void delete(String name) {
        table.remove(name);
    }

    public void display() {
        if (table.isEmpty()) {
            System.out.println("Symbol Table is empty");
        } else {
            for (Identifier id : table.values()) {
                System.out.println(id.getName() + " : " + id.getType());
            }
        }
    }
}

public class SymbolTable {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        SymbolTableManager st = new SymbolTableManager();

        while (true) {
            System.out.println("\n1.Insert\n2.Lookup\n3.Delete\n4.Display\n5.Exit");
            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter identifier: ");
                    String name = sc.nextLine();
                    System.out.print("Enter type: ");
                    String type = sc.nextLine();
                    st.insert(new Identifier(name, type));
                    break;
                case 2:
                    System.out.print("Enter identifier: ");
                    String search = sc.nextLine();
                    Identifier result = st.lookup(search);
                    if (result != null) {
                        System.out.println(result.getName() + " : " + result.getType());
                    } else {
                        System.out.println("Not Found");
                    }
                    break;
                case 3:
                    System.out.print("Enter identifier: ");
                    String del = sc.nextLine();
                    st.delete(del);
                    break;
                case 4:
                    st.display();
                    break;
                case 5:
                    System.exit(0);
            }
        }
    }
}