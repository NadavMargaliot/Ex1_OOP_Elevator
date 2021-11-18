import ex1.Ex1_main;

public class Ex1_tester {
    public static void main(String[] args) {
     B5 = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B5.json"
     calls_d = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_d.csv"

        if(args==null || args.length<4) {
            args = new String[4];
            args[0] = "123456789";
            args[1] = B5;
            args[2] = "/Users/adielbenmeir/PycharmProjects/OOP_2021/Assignments/Ex1/src/output.csv";
            long time = System.currentTimeMillis();
            args[3] = "out/Ex1_report_case_" + "_" + time + "_ID_.log";
        }
        Ex1_main.main(args);
    }
}
