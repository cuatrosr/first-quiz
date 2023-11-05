package org.velezreyes.quiz.question6;

import java.util.List;

public class VendingMachineImpl implements VendingMachine {
    private static VendingMachine instance;
    private static List<Drink> drinks;
    private static int quarters;

    public static VendingMachine getInstance() {
        return instance == null ? instance = new VendingMachineImpl() : instance;
    }

    public VendingMachineImpl() {
        drinks = List.of(new DrinkImpl("ScottCola", true, 3), new DrinkImpl("KarenTea", false, 4));
        quarters = 0;
    }

    @Override
    public void insertQuarter() {
        quarters++;
    }

    private void decreaseQuarters(int amount) {
        quarters -= amount;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
      Drink drink = validateDrink(name);
      validateQuarters(drink);
      decreaseQuarters(drink.getPrice());
      return drink;
    }

    private Drink validateDrink(String name) throws UnknownDrinkException {
      return drinks.stream().filter(drink -> drink.getName().equals(name)).findFirst().orElseThrow(UnknownDrinkException::new);
    }

    private void validateQuarters(Drink drink) throws NotEnoughMoneyException {
      if (quarters < drink.getPrice()) throw new NotEnoughMoneyException();
    }
}
