import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        resposta();
    }

    public static void resposta(){
        System.out.println("Qual o Salário Base? (coloque apenas o número bruto e use '.' ao invés de ','): ");
        Scanner one = new Scanner(System.in);
        Dados cheque = new Dados();

        cheque.salario_base = one.nextDouble();

        System.out.println("Referência em dia:");
        cheque.dia = one.nextDouble();

        System.out.println("Referência em hora:");
        cheque.hora = one.nextDouble();


        System.out.println("Dia do mês da admissião:");
        cheque.data_admi = one.nextDouble();

        Main calculo = new Main();



        calculo.vencimentos(cheque, calculo);
        //calculo.inss(salario_base);


    }

    public static void descontos(Dados cheque, Main calculo){

        System.out.println("Quantos dias o funcionário faltou? ");
        Scanner one = new Scanner(System.in);
        cheque.dias_falta = one.nextDouble();


        cheque.falta = cheque.salario_base/cheque.dia;

        cheque.falta = cheque.falta * cheque.dias_falta;

        cheque.remuneracao = cheque.remuneracao - cheque.falta;

        cheque.vale_transporte = 0;

        //Vale transporte
        System.out.println("O funcionário teve Vale Transporte? (1)-Sim e (0)-Não ");
        Scanner two = new Scanner(System.in);
        int vt = two.nextInt();
        if (vt == 1){
            cheque.vale_transporte = cheque.salario_base * 0.06;
        }

        calculo.inss(cheque, calculo);


    }



    public static void vencimentos(Dados cheque, Main calculo){
        System.out.println("Quantas horas extras o funcionário fez? ");
        Scanner one = new Scanner(System.in);
        cheque.n_hora = one.nextDouble();

        cheque.valor_hora = cheque.salario_base/cheque.hora;
        cheque.hora_extra = cheque.n_hora * cheque.valor_hora;

        double x = cheque.dia + 1 - cheque.data_admi;

        cheque.remuneracao = cheque.salario_base/cheque.dia;
        cheque.remuneracao = cheque.remuneracao * x;

        calculo.descontos(cheque, calculo);

    }

    public static void inss(Dados cheque, Main calculo){

        INSS n1 = new INSS();
        double inss1 = 0;
        double inss2 = 0;
        double inss3 = 0;
        double inss4 = 0;
        double inss_total = 0;
        cheque.remuneracao = cheque.remuneracao + cheque.hora_extra;
        if ( cheque.remuneracao <= n1.base1){
            inss_total = cheque.remuneracao * 0.075;
        }
        if ( cheque.remuneracao > n1.base1 && cheque.remuneracao <= n1.base2){
            inss1 = n1.base1 * 0.075;
            inss2 = cheque.remuneracao - n1.base1;
            inss2 = inss2 * 0.09;
            inss_total = inss1 + inss2;
        }

        if ( cheque.remuneracao > n1.base2 && cheque.remuneracao <= n1.base3){
            inss1 = n1.base1 * 0.075;
            inss2 = n1.base2 - n1.base1;
            inss2 = inss2 * 0.09;
            inss3 = cheque.remuneracao - n1.base2;
            inss3 = inss3 * 0.12;
            inss_total = inss1 + inss2 + inss3;
        }

        if ( cheque.remuneracao > n1.base3 && cheque.remuneracao <= n1.base4){
            inss1 = n1.base1 * 0.075;
            inss2 = n1.base2 - n1.base1;
            inss2 = inss2 * 0.09;
            inss3 = n1.base3 - n1.base2;
            inss3 = inss3 * 0.12;
            inss4 = cheque.remuneracao - n1.base3;
            inss4 = inss4 * 0.14;
            inss_total = inss1 + inss2 + inss3 + inss4;
        }
        double liquido = cheque.remuneracao - cheque.vale_transporte - inss_total;



        System.out.println("");

        System.out.println("Salário Base : R$" + cheque.salario_base);
        System.out.println("Remuneração  : R$" + cheque.remuneracao);
        System.out.println("Valor líquido: R$" + liquido);
        System.out.println("Inss         : R$" + inss_total);
        System.out.println("V.T          : R$" + cheque.vale_transporte);
        System.out.println("Fgts         : R$" + cheque.remuneracao * 0.08);

        //n1.calculo(inss1);
    }
}