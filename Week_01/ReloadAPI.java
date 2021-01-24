import java.util.Deque;
import java.util.LinkedList;

// import jdk.internal.vm.PostVMInitHook;

public class ReloadAPI {
    public static void main(String[] args) {
        Deque<String> deque = new LinkedList<String>();

        deque.addLast("a");
        deque.addLast("b");
        deque.addLast("c");
        System.out.println(deque);

        String str = deque.peekLast();
        System.out.println(str);
        System.out.println(deque);

        while (deque.size() > 0) {
            System.out.println(deque.removeLast());
        }
        System.out.println(deque);

    }
}