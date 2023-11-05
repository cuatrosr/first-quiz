package org.velezreyes.quiz.question6;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public class DrinkImpl implements Drink {
    private String name;
    private boolean fizzy;
    private int price;
}
