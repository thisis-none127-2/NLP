import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class DFA {
    private Set<Integer> states;
    private Set<Character> alphabet;
    private int startState;
    private Set<Integer> acceptStates;

    public DFA(Set<Integer> states, Set<Character> alphabet, int startState, Set<Integer> acceptStates) {
        this.states = states;
        this.alphabet = alphabet;
        this.startState = startState;
        this.acceptStates = acceptStates;
    }

    private int transition(int state, char input) {
        if (state == 0 && input == 'a') return 1;
        if (state == 1 && input == 'b') return 2;
        if (state == 2 && input == 'b') return 2;
        return -1;
    }

    public boolean accept(String input) {
        int currentState = startState;
        for (char c : input.toCharArray()) {
            if (!alphabet.contains(c)) return false;
            currentState = transition(currentState, c);
            if (currentState == -1) return false;
        }
        return acceptStates.contains(currentState);
    }
}

public class DFAAcceptance {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Set<Integer> states = new HashSet<>();
        states.add(0);
        states.add(1);
        states.add(2);

        Set<Character> alphabet = new HashSet<>();
        alphabet.add('a');
        alphabet.add('b');

        int startState = 0;

        Set<Integer> acceptStates = new HashSet<>();
        acceptStates.add(2);

        DFA dfa = new DFA(states, alphabet, startState, acceptStates);

        System.out.print("Enter string: ");
        String input = sc.nextLine();

        if (dfa.accept(input)) {
            System.out.println("Accepted");
        } else {
            System.out.println("Rejected");
        }
    }
}