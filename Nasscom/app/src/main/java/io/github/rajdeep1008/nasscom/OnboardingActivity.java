package io.github.rajdeep1008.nasscom;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentStatePagerAdapter;
import android.support.v4.view.PagerAdapter;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.pixelcan.inkpageindicator.InkPageIndicator;

public class OnboardingActivity extends AppCompatActivity {

    private static final int NUM = 3;
    private ViewPager viewPager;
    private PagerAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_onboarding);

        viewPager = (ViewPager) findViewById(R.id.onboard_pager);
        adapter = new OnboardPagerAdapter(getSupportFragmentManager());
        viewPager.setAdapter(adapter);
    }

    private class OnboardPagerAdapter extends FragmentStatePagerAdapter {

        public OnboardPagerAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int position) {
            return OnboardFragment.getInstance(position);
        }

        @Override
        public int getCount() {
            return NUM;
        }
    }
}
