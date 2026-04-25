import java.util.*;

class NFA {
    private Map<Integer, Map<Character, Set<Integer>>> transitions = new HashMap<>();
    private int startState;
    private Set<Integer> acceptStates;

    public NFA(int startState, Set<Integer> acceptStates) {
        this.startState = startState;
        this.acceptStates = acceptStates;
    }

    public void addTransition(int from, char input, int to) {
        transitions
            .computeIfAbsent(from, k -> new HashMap<>())
            .computeIfAbsent(input, k -> new HashSet<>())
            .add(to);
    }

    public boolean accept(String input) {
        Set<Integer> currentStates = new HashSet<>();
        currentStates.add(startState);

        for (char c : input.toCharArray()) {
            Set<Integer> nextStates = new HashSet<>();
            for (int state : currentStates) {
                if (transitions.containsKey(state) && transitions.get(state).containsKey(c)) {
                    nextStates.addAll(transitions.get(state).get(c));
                }
            }
            currentStates = nextStates;
        }

        for (int state : currentStates) {
            if (acceptStates.contains(state)) return true;
        }
        return false;
    }
}

public class NFAAcceptance {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Set<Integer> acceptStates = new HashSet<>();
        acceptStates.add(2);

        NFA nfa = new NFA(0, acceptStates);

        nfa.addTransition(0, 'a', 0);
        nfa.addTransition(0, 'a', 1);
        nfa.addTransition(1, 'b', 2);

        System.out.print("Enter string: ");
        String input = sc.nextLine();

        if (nfa.accept(input)) {
            System.out.println("Accepted");
        } else {
            System.out.println("Rejected");
        }
    }
}