package io.github.rajdeep1008.nasscom;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.LinearSnapHelper;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.SnapHelper;
import android.view.View;

import java.util.ArrayList;
import java.util.List;

public class BadgeActivity extends AppCompatActivity {

    RecyclerView first, second, third;
    BadgeAdapter adapterOne, adapterTwo, adapterThree;
    List<Badge> badgeList, list2, list3;
    SnapHelper snapHelper, snapHelper2, snapHelper3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_badge);

        first = (RecyclerView) findViewById(R.id.first);
        second = (RecyclerView) findViewById(R.id.second);
        third = (RecyclerView) findViewById(R.id.third);

        first.setHasFixedSize(true);
        second.setHasFixedSize(true);
        third.setHasFixedSize(true);

        snapHelper = new LinearSnapHelper();
        snapHelper2 = new LinearSnapHelper();
        snapHelper3 = new LinearSnapHelper();

        snapHelper.attachToRecyclerView(first);
        snapHelper2.attachToRecyclerView(second);
        snapHelper3.attachToRecyclerView(third);

        badgeList = new ArrayList<>();
        badgeList.add(new Badge(R.drawable.blr1));
        badgeList.add(new Badge(R.drawable.del1));
        badgeList.add(new Badge(R.drawable.hyd1));
        badgeList.add(new Badge(R.drawable.pun1));

        list2 = new ArrayList<>();
        list2.add(new Badge(R.drawable.tbg));
        list2.add(new Badge(R.drawable.gameon));
        list2.add(new Badge(R.drawable.tierup));

        list3 = new ArrayList<>();
        list3.add(new Badge(R.drawable.blr2));
        list3.add(new Badge(R.drawable.del2));
        list3.add(new Badge(R.drawable.hyd2));
        list3.add(new Badge(R.drawable.pun2));

        adapterOne = new BadgeAdapter(badgeList, this);
        adapterTwo = new BadgeAdapter(list2, this);
        adapterThree = new BadgeAdapter(list3, this);

        first.setLayoutManager(new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false));
        first.setAdapter(adapterOne);

        second.setLayoutManager(new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false));
        second.setAdapter(adapterTwo);

        third.setLayoutManager(new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false));
        third.setAdapter(adapterThree);

    }
}
