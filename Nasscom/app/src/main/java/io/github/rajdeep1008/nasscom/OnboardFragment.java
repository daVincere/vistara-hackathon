package io.github.rajdeep1008.nasscom;


import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;


public class OnboardFragment extends Fragment {

    int position;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_onboard, container, false);

        position = getArguments().getInt("position");
        switch (position) {

        }

        return view;
    }

    public static Fragment getInstance(int pos) {
        OnboardFragment fragment = new OnboardFragment();
        Bundle bundle = new Bundle();
        bundle.putInt("position", pos);
        fragment.setArguments(bundle);

        return fragment;
    }
}
